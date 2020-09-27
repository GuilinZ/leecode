##backward思想
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False

##进阶 将tx-=ty的操作合并到一步
# class Solution {
# public:
#   bool reachingPoints(int sx, int sy, int tx, int ty) {
#     while (sx <= tx && sy <= ty) {
#       if (sx == tx && (ty - sy) % tx == 0) return true;
#       if (sy == ty && (tx - sx) % ty == 0) return true;
#       if (tx < ty) ty %= tx;
#       else tx %= ty;
#     }
#     return false;
#   }
# };