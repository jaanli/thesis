import torch
import data
class InnerProduct(torch.nn.Module):
  def __init__(self, n_users, n_items, n_attr, emb_size):
    super().__init__()
    self.user_embeddings = torch.nn.Embedding(n_users, emb_size)
    self.attribute_emb = torch.nn.EmbeddingBag(n_attr, emb_size)
    self.item_embeddings = torch.nn.Embedding(n_items, emb_size)
    self.intercepts = torch.nn.Embedding(n_items, 1)
  def forward(self, users, items, item_attributes, offsets):
    user_emb = self.user_embeddings(users)
    attr_emb = self.attribute_emb(item_attributes, offsets)
    item_emb = self.item_embeddings(items)
    logits = (user_emb * (attr_emb + item_emb)).sum(-1)
    return logits + self.intercepts(items).squeeze()
train = data.load(batch_size=2 ** 16) # negative labels in last half of every batch
model = InnerProduct(train.n_users, train.n_items, train.n_attr, 100)
optim = torch.optim.SGD(model.parameters(), learning_rate=15.0)
loss = torch.nn.BCEWithLogitsLoss()
labels = (torch.arange(2 ** 16) < (2 ** 16 / 2)).float()
for batch in train:
  model.zero_grad()
  logits = model(*batch)
  L = loss(logits, labels)
  L.backward()
  optim.step()