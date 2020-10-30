#ベースイメージ
FROM python:3.7.2

#Dockerfileと同ディレクトリにあるappフォルダをコンテナ内部へ追加
ADD app /app

#Dockerfileビルド時に実行されるコマンド
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# workdirectory 作成
WORKDIR /app

#コンテナ起動時に実行されるコマンド
CMD python -u main.py
