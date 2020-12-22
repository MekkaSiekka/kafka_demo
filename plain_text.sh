AKIATUMF76J24LSPOKD5

aws kafka describe-cluster --region us-east-1 --cluster-arn "




arn:aws:kafka:us-east-1:249925988981:cluster/AWSKafkaTutorialCluster/1dce9319-f050-473f-ad06-ce6549b36581-2


"z-2.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:2181,z-1.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:2181,z-3.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:2181" --replication-factor 3 --partitions 1 --topic AWSKafkaTutorialTopic 


bin/kafka-topics.sh --create --zookeeper ZookeeperConnectString --replication-factor 3 --partitions 1 --topic AWSKafkaTutorialTopic


aws kafka get-bootstrap-brokers --region us-east-1 --cluster-arn "arn:aws:kafka:us-east-1:249925988981:cluster/AWSKafkaTutorialCluster/1dce9319-f050-473f-ad06-ce6549b36581-2"


{
    "BootstrapBrokerStringTls": "b-1.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialcluste.kyzzi1.c2.kafka.us
-east-1.amazonaws.com:9094,b-3.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094"
}

./kafka-console-producer.sh --broker-list BootstrapBrokerStringTls --producer.config client.properties --topic AWSKafkaTutorialTopic

./kafka-console-producer.sh --broker-list "b-1.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094,b-3.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094" --producer.config client.properties --topic AWSKafkaTutorialTopic


./kafka-console-consumer.sh --bootstrap-server "b-1.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094,b-2.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094,b-3.awskafkatutorialcluste.kyzzi1.c2.kafka.us-east-1.amazonaws.com:9094"  --consumer.config client.properties --topic AWSKafkaTutorialTopic --from-beginning



#https://aws.amazon.com/blogs/compute/using-amazon-msk-as-an-event-source-for-aws-lambda/