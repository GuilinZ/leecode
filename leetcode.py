


def Leetcode_200:
	number of islands
	DFS
	先定义一个dfs,目的是当遇到'1'时,开始搜索所有相邻的'1',然后标注为'0'.在main里,每trigger一次dfs,answer就+=1
def Leetcode_3:
	Longest Substring without repeating characters
	Sliding window 代替循环
	检查是否有重复字母用hashmap
	类似于twosum,如果s[j]不在map里,加入s[j],j+=1, 更新answer长度
	如果在map里,remove掉map第一个item,i+=1
def Leetcode_124:
	Binary Tree Maximum Path Sum
	定义了max_gain, 递归求当前node和其中一个subtree能得到的sum的最大值. return的是node.val+max(left_gain,right_gain)
	但是同时引入了一个量,price = node.val+left_gain,right_gain
	这个值是真正的以此node为顶点,从左到右的path的sum
	更新这个值,找到最大
def Leetcode_104:
	124简化版,直接秒
	注意recursion一般有两个return, 第一个是node==None时,return 0
	第二个是return真正想要累加的目标值,一般是当前node的val+(left or right)
def Leetcode_111:
	104镜像问题,稍微复杂一些,考虑如果有一边的subtree为None时,要继续计算右边的深度,不能在这里停下. 都不为0时,累加规则为cur_depth = 1+min(left_depth,right_depth)
	left_depth 和 right_depth都由递归minDepth函数求得