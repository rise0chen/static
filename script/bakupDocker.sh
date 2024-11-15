img=$1
new_name=$2
if [ -z $new_name ]
then
    new_name=$img
fi

echo "backup $img to $new_name"
docker pull $img
docker tag $img registry.cn-shanghai.aliyuncs.com/lebai/$new_name
docker push registry.cn-shanghai.aliyuncs.com/lebai/$new_name
