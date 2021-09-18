# Câu chuyện:
# 
# Sau khi gặp được William và biết được William cũng là một thực tập sinh trong chương trình năm nay,
# bạn Trẩu nhận ra rằng ngoài mình ra còn có nhiều bạn thực tập sinh khác.
# Do đó, Trẩu và William đã tổ chức một cuộc thi văn nghệ để giao lưu kết bạn với nhau.
# Trong buổi thi hát, Trẩu và William đã thi hát với nhau và nhờ các bạn thực tập sinh khác bình chọn.
# Người được bình chọn nhiều nhất sẽ hát tặng thêm một bài cho khán giả.
# Để việc kiểm tra phiếu được công bằng,
# chúng ta hãy giúp Trẩu viết một hàm để đếm số phiếu và cho biết ai là người hát được mọi người yêu thích nhất.
# 
# Yêu cầu:
# 
# Viết một hàm who_is_winner(votes) nhận vào một mảng lưu lượt bình chọn của các bạn thực tập sinh khác.
# 
# Hàm này sẽ trả về "Trau" nếu Trẩu là người có bình chọn nhiều hơn; hoặc "William"
# nếu William có lượt bình chọn nhiều hơn; hoặc "Both" nếu Trẩu và William có cùng lượt bình chọn.
# 
# Học sinh chỉ nộp hàm who_is_winner(votes).

def who_is_winner(votes):
    count_votes_trau = 0
    count_votes_william = 0
    for name in votes:   
        if name == 'Trau':
            count_votes_trau = count_votes_trau + 1
        else:
            count_votes_william = count_votes_william + 1
    if count_votes_trau == count_votes_william:
        return 'Both'
    elif count_votes_trau > count_votes_william:
        return 'Trau'
    else:
        return 'William'
  