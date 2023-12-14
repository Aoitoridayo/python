from memo import Memo

class MemoManager:
    def __init__(self):
        self.memo_list = [
            Memo('First memo', 'This is the first memo.'),
            Memo('Second memo', 'This is the second memo.'),
            Memo('Third memo', 'This is the third memo.')
        ]

    def add_memo(self, title: str, content: str) -> Memo:
        memo = Memo(title, content)
        self.memo_list.append(memo)
        return memo

    def get_memo(self, memo_id: str) -> Memo:
        for memo in self.memo_list:
            if memo.id == memo_id:
                return memo
        return None

    def get_all_memos(self) -> list[Memo]:
        return self.memo_list

    def delete_memo(self, memo_id) -> Memo:
        for memo in self.memo_list:
            if memo.id == memo_id:
                self.memo_list.remove(memo)
                return memo
        return None
    
