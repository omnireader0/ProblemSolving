class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val head = ListNode(0)
        var p = l1
        var q = l2
        var cur = head
        var cnt = 0

        while (q != null || p != null) {
            val x = p?.`val` ?: 0
            val y = q?.`val` ?: 0

            val temp = x+y+cnt
            cnt = temp/10
            cur.next = ListNode(temp%10)
            cur = cur.next
            if (p != null) p = p?.next
            if (q != null) q = q?.next
        }
        if (cnt > 0) {
            cur.next = ListNode(cnt)
        }
        return head.next
    }
}
