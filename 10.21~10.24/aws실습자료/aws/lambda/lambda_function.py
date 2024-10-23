import boto3
import pandas as pd
import matplotlib.pyplot as plt
import io


s3 = boto3.client('s3',
                  aws_access_key_id='your_access_key',
                  aws_secret_access_key='your_secret_access_key')




def lambda_handler(event, context):
    # S3 이벤트로부터 버킷 이름과 파일 키를 가져온다
    print(event)
    #bucket_name = "aws-lec-test"
    #file_key = "student.csv"
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    print(bucket_name)
    print(file_key)
    
    # S3에서 CSV 파일을 다운로드하여 데이터프레임으로 읽어들인다
    csv_file = s3.get_object(Bucket=bucket_name, Key=file_key)
    df = pd.read_csv(csv_file['Body'])
    
    print('df_run')
    # 데이터 분석을 수행 (여기서는 예시로 간단히 데이터 요약을 사용)
    summary = df.describe()
    print('summary_run')
    
    # 시각화를 수행 (여기서는 예시로 히스토그램을 사용)
    plt.figure()
    df.hist()
    plt.tight_layout()
    print('plt_run')
    
    # 시각화 결과를 PNG 이미지로 저장
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    print('img_run')
    
    # S3에 시각화 결과 업로드
    output_file_key = file_key.replace('.csv', '_visualization.png')
    s3.put_object(Bucket=bucket_name, Key=output_file_key, Body=img_data, ContentType='image/png')
    print('s3_run')
    
    return {
        'statusCode': 200,
        'body': f'Successfully processed and visualized {file_key} and saved to {output_file_key}'
    }