from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_cors import CORS
import pymysql
import uuid



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
# # MySQL 데이터베이스 설정
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/bonnews'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

# # SQLAlchemy 객체 생성
# db = SQLAlchemy(app)

# # 모델 정의
# class News(db.Model):
#     __tablename__ = 'news'

#     uuid = db.Column(db.String(36), primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     content = db.Column(db.String, nullable=False)
#     writer = db.Column(db.String, nullable=False)
#     created = db.Column(db.String, nullable=False)
#     showed = db.Column(db.Integer, nullable=False)
#     titleImg = db.Column(db.String(36), db.ForeignKey('img.uuid'), nullable=False)
#     imgArr = db.Column(db.String, nullable=False)

#     img = relationship("Img", back_populates="news") 

# class Img(db.Model):
#     __tablename__ = 'img'

#     uuid = db.Column(db.String(36), primary_key=True)
#     src = db.Column(db.String, nullable=False)

#     news = relationship("News", back_populates="img") 



# # 라우트 정의
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/news') 
# def news_load():
#     # 데이터베이스에서 뉴스 목록을 가져와 출력
#     news_list = News.query.all()
#     news_data = []
#     for item in news_list:
#         img_src = item.img.src if item.img else None
#         news_data.append({
#             'uuid': item.uuid,
#             'title': item.title,
#             'showed': item.showed,
#             'img_src': img_src  # 이미지의 src 값 추가
#         })

#     return jsonify(news_data)

# @app.route('/news/<string:news_id>', methods=['GET'])
# def get_news(news_id):
#     news = News.query.get_or_404(news_id)
#     img_array = []
#     for img_uuid in news.imgArr.split(','):  # imgArr은 쉼표로 구분된 문자열이므로 split() 사용
#         img = Img.query.get(img_uuid.strip())  # 공백 제거
#         if img:
#             img_array.append(img.src)
    
#     return jsonify({
#         'title': news.title,
#         'content': news.content,
#         'created': news.created,
#         'writer': news.writer,
#         'titleImg': news.img.src,
#         'imgArr': img_array
#     })

# @app.route('/write', methods=['POST'])
# def add_news():
#     if request.method == 'POST':
#         try:
#             data = request.json

#             # 필수 필드 유효성 검사
#             required_fields = ['title', 'content', 'writer', 'created', 'titleImg', 'imgArr']
#             for field in required_fields:
#                 if field not in data:
#                     return jsonify({'error': f'필수 필드 누락: {field}'}), 400
                
#             img_array = []
            
#             if len(data['imgArr']) > 0:
#                 for item in data['imgArr']:
#                     uid = uuid.uuid4()
#                     img_array.append(uid)
#                     new_img = Img(
#                         uuid=uid,
#                         src=item
#                     )
#                     db.session.add(new_img)
#                 db.session.commit()

#             title_img_uuid = uuid.uuid4() if data['titleImg'] != "" else None
            
#             new_news = News(
#                 title=data['title'],
#                 content=data['content'],
#                 writer=data['writer'],
#                 created=data['created'],
#                 showed=1,
#                 titleImg=title_img_uuid,
#                 imgArr=','.join(str(img.uuid) for img in img_array)  # 이미지 UUID들을 쉼표로 구분된 문자열로 변환
#             )
#             if title_img_uuid is not None:
#                 new_title_img = Img(
#                 uuid=title_img_uuid,
#                 src=data['titleImg']
#                 )
#                 db.session.add(new_title_img)
#                 db.session.commit()
            

#             db.session.add(new_news)
#             db.session.commit()

#             return jsonify({'message': '뉴스가 성공적으로 추가되었습니다!'})

#         except Exception as e:
#             print(f"뉴스 추가 중 오류: {str(e)}")
#             return jsonify({'error': '내부 서버 오류'}), 500

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run(debug=True)
