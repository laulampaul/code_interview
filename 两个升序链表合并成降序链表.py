    def helper2(self,l1,l2):
        i=l1
        j=l2
        cur=None

        while i!=None or j!=None:
            
            if i==None:
                print(j.val)
                post=j.next
                j.next=cur
                cur=j
                j=post
            elif j==None:
                print(i.val)
                post=i.next
                i.next=cur
                cur=i
                i=post
            elif i.val<j.val:
                print(i.val,j.val)
                post=i.next
                i.next=cur
                cur=i
                i=post
            else:
                print(i.val,j.val)
                post=j.next
                j.next=cur
                cur=j
                j=post

        return cur
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if l1==None and l2==None:
                return None
            return self.helper2(l1,l2)
