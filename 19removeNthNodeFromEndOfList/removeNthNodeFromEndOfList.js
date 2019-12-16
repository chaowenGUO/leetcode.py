/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let [fast, slow] = Array(2).fill(head)
    for (let _ = 0; !Object.is(_, n); ++_) fast = fast.next
    if (!fast) return head.next
    else
    {
        while (fast.next)
        {
            fast = fast.next
            slow = slow.next
        }
        slow.next = slow.next.next
        return head
    }
};
