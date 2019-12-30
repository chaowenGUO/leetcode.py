/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        final ArrayList<List<Integer>> result = new ArrayList<>();
        List<TreeNode> level = Arrays.asList(root);
        while (root != null && !level.isEmpty())
        {
            result.add(level.stream().map(node -> node.val).collect(Collectors.toList()));
            level = level.stream().flatMap(node -> Stream.of(node.left, node.right)).filter($ -> $ != null).collect(Collectors.toList());
        }
        Collections.reverse(result);
        return result;
    }
}