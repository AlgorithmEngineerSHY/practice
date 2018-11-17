class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name:
            return True
        idx_name = idx_type = 0
        while idx_name < len(name) and idx_type < len(typed):
            if name[idx_name] == typed[idx_type]:
                idx_name += 1
                idx_type += 1
            else:
                idx_type += 1
        if idx_name == len(name):
            return True
        else:
            return False

