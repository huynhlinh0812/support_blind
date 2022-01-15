def intent(text):
	if "thêm email" in text or "add email" in text or "thêm gmail" in text or "add gmail" in text or "add mail" in text or "thêm mail" in text:
		return 2
	elif "email" in text or "mail" in text or "gmail" in text:
		return 3
	elif "thời tiết" in text or "trời hôm nay" in text or "weather" in text:
		return 4
	elif "nghe nhạc" in text or "âm nhạc" in text or "chơi nhạc" in text or "music" in text:
		return 5
	elif "mấy giờ" in text or "thời gian" in text or "time" in text:
		return 6
	elif "tin tức" in text or "watch news" in text:
		return 7
	elif "thêm số điện thoại" in text or "thêm số nhắn tin" in text or "thêm số người gửi tin nhắn" in text or "" or "add phone" in text:
		return 8
	elif "tin nhắn" in text or "nhắn tin" in text or "message" in text:
		return 9
	elif "đọc báo" in text or "read news" in text:
		return 10
	elif "tra từ điển" in text or "định nghĩa từ" in text or "từ này nghĩa là gì" in text or "define" in text:
		return 11
	elif "đọc tài liệu" in text or "đọc" in text or "document" in text:
		return 12 
	elif "bao nhiêu nam và bao nhiêu nữ" in text or "có bao nhiêu người ở phía trước" in text or "phía trước có bao nhiêu người" in text or "đằng trước có bao nhiêu người" in text or "có bao nhiêu người" in text or "bao nhiêu nam nữ" in text or "bao nhiêu năm và bao nhiêu nữ" in text or "nhiêu người ở phía trước" in text or "how many people are there" in text:
		return 13
	elif "thêm người liên hệ" in text or "thêm người gửi tin nhắn" in text or "thêm người quen" in text or "add more acquaintance" in text:
		return 14
	elif "phía trước là ai" in text or "đằng trước là ai" in text or "trước mặt là ai" in text or "có ai ở phía trước" in text or "trước mặt có ai" in text or "ai ở đằng trước" in text or "trước mặt là ai" in text:
		return 15
	elif "thêm hướng dẫn" in text or "dạy học" in text or "dạy bạn học" in text or "hướng dẫn bạn cái này" in text or "tutorial" in text:
		return 16
	elif "có gì ở phía trước" in text or "có gì ở đằng trước" in text or "có gì trước mặt" in text or "có gì ở đó" in text:
		return 17
	elif "hướng dẫn" in text or "chỉ mình cái này với" in text or "chỉ tôi" in text or "add tutorial" in text:
		return 18
	elif "dừng" in text or "tạm biệt" in text or "bye" in text or "stop" in text:
		return 19
