# 28. 해시맵 디자인
# 풀이 1

import collections

class MyHashMap:
    def __init__(self):
        self.size = 1000    # 기본 사이즈
        self.table = collections.defaultdict(ListNode)  
        # defaultdict: 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우(충돌) 연결 리스트 처리
        # 개별 체이닝 방식
        p = self.table[index]
        while p:
            if p.key == key:    # 이미 key가 존재할 경우 업데이트
                p.value = value
                return
            if p.next is None:  # 마지막이라면 루프 break
                break
            p = p.next
        p.next = ListNode(key, value)


    # 조회
    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            # p가 유일한 노드일 때 ListNode()로 빈 노드 할당(defualtdict 이므로)
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# 개별 체이닝 방식을 위한 연결 리스트 클래스
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None