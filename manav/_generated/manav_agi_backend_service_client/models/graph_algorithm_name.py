from enum import StrEnum


class GraphAlgorithmName(StrEnum):
    BETWEENNESS_CENTRALITY = "betweenness_centrality"
    DIJKSTRA = "dijkstra"
    LOUVAIN = "louvain"
    NODE_SIMILARITY = "node_similarity"
    PAGERANK = "pagerank"

    def __str__(self) -> str:
        return str(self.value)
