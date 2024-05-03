class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_segments = version1.split('.')
        v2_segments = version2.split('.')
        
        for i in range(max(len(v1_segments), len(v2_segments))):
            v1_val = int(v1_segments[i]) if i < len(v1_segments) else 0
            v2_val = int(v2_segments[i]) if i < len(v2_segments) else 0
            
            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1
        
        return 0