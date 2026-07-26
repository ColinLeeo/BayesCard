# Gcard artifact changes

This branch carries the multi-table BayesCard implementation that was
previously distributed with the public SafeBound artifact.  It adds the join
ensemble, query-factor preparation, STATS schema, and the bundled `pgympy`
compatibility module required by the Gcard relational adapters.

Experiment orchestration, dataset paths, and result handling intentionally
live in the parent Gcard artifact repository.  This fork contains no generated
models, catalogs, datasets, or machine-specific paths.
