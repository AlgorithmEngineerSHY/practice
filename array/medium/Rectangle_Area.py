class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(D, H) - max(B, F), 0) * max((min(C, G) - max(A, E)), 0)
        return (C - A) * (D - B) + (H - F) * (G - E) - overlap
