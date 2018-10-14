# LCA_DAG_test.py

import pytest
import LCA_DAG

## coverage py.test --cov lca_dag.py test

# check printTree works
def test_BFS():
    result = LCA_DAG.BFS(LCA_DAG.testDAG, 1, 9)
    assert list(result) == [[1, 3, 9]]