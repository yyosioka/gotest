#�x�[�X�C���[�W
FROM python:3.7.13

#Dockerfile�Ɠ��f�B���N�g���ɂ���app�t�H���_���R���e�i�����֒ǉ�
ADD app /app

#Dockerfile�r���h���Ɏ��s�����R�}���h
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# workdirectory �쐬
WORKDIR /app

#�R���e�i�N�����Ɏ��s�����R�}���h
CMD python -u main.py
