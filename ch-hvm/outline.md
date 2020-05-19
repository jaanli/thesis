Hierarchical variational models in statistical physics

# intro

- summarize mean field methods in statistical physics

- describe the computational goals in statistical physics models: computing physical quantities (e.g. specific heat, magnetization) from a hamiltonian (and corresponding boltzmann distribution) that describes a system.

- describe how those goals are achieved. (1) markov chain monte carlo. expectations approximated by samples from the boltzmann distribution. (2) mean field methods

- describe the wu 2019 paper. this paper frames the problem in terms of policy gradients and reinforcement learning.

- describe the contributions of our paper: (1) show that gibbs-bogoliubov-feynman inequality is equivalent to variational inference. (1) show how the reinforcement learning approach of wu (2019) is more naturally expressed in terms of variational inference. (2) show that a modern tool of variational inference, HVMs, is useful and improves on wu (2019) by scaling to larger system sizes.

# background: the gibbs-bogoliubov-feynman equation as variational inference

- describe the variational principle in statistical physics: the gibbs-bogoliubov-feynman inequality that relates the partition function of a mean-field system to the partition function of the model of interest

- describe variational inference in machine learning, using the language of probability models and the evidence lower bound terminology

- paragraph on how they are the same thing; mapping concepts from one to the other. cite papers using gibbs-bogoliubov-feynman for markov fields in 1994, and then the VI historic literature from the SVI paper lit review

- by the end of this section, the reader should be clear about what a model is, what data is, what samples are, that spins are random (latent) variables. 

- make a note that we stick to maximizing a lower bound on free energy, as is standard in gibbs-bogoliubov-feynman and variational inference 

# background: black box variational inference 

- how to optimize the lower bound via gradients, and why this is worthwhile (neural networks; generic methods but accurate solutions). cite shakir's recent review for gradient estimation.

- describe black box variational inference. 

# background: variational families 

- describe fully factorized mean-field distribution that all readers will be familiar with. (eq 3.42, wainwright & jordan 2008)

- describe bethe approximation as minimizing variational free energy, but over the local polytope that is pairwise consistent, not the marginal polytope. 

- describe wu (2019) as using a variational distribution parameterized by an autoregressive neural network. correlated, but expensive to sample from.

- next, we describe hierarchical variational models - combine benefits of mean-field (fast to compute) with benefits of methods like wu (2019) (slow, but accurate)

# method: hierarchical variational models

- describe variational family, with diagram

- derive hierarchical bound on free energy.

# experiments

- figure for ising model at several temperatures, accuracy vs time for L=16, 32, 64

- figure for SK model at several temperatures, accuracy vs time

# discussion

- say it's not as accurate as wu (2019), leading to a tradeoff of system sizes

- future work: hierarchical latent variables allow variational families with physics-based priors (such as nearest-neighbor convolution structure)

# appendix

- any notes on glossary of machine learning vs physics terminology that isn't appropriate for the background section





