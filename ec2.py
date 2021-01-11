import boto3

client = boto3.client('ec2')

def get_ec2_all():
   try:
        instances = []
        response = client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_name = instance['Tags'][0]['value']
                instance_type = instance['InstanceType']
                instance_key_name = instance['KeyName']
                instance_state_name = instance['State']['Name']
                instance_privateip = instance['PrivateIpAddress']
                temp_dict = {}
                temp_dict['instance_id'] = instance_id
                temp_dict['instance_name'] = instance_name
                temp_dict['instance_type'] = instance_type
                temp_dict['instance_key_name'] = instance_key_name
                temp_dict['instance_state_name'] = instance_state_name
                temp_dict['instance_privateip'] = instance_privateip
                instances.append(temp_dict)
            return instances
   except:
        print('Não foi possível obter informações das Instância EC2. Rode o comando aws configure e valide suas credenciais')

def ec2_name_filter_by_id(instance_id):
    try:
        response = client.describe_instances(InstanceIds = [instance_id])
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_name = instance['Tags'][0]['Value']
                return instance_name
    except:
        print('Não foi possível obter informações do EC2. Tente novamente')

def poweroff_ec2(instance_id):
    try:
        response = client.stop_instances(
            InstanceIds = [instance_id]
        )
        current_state = response['StoppingInstances'][0]['CurrentState']['Name']
        previous_state = response['StoppingInstances'][0]['PreviousState']['Name']
        message = f'InstanceId: {instance_id} current state is {current_state} and previous state was {previous_state}'
        return message
    except:
        print('Não foi possível dar um stop na instância. Tente novamente')

def poweron_ec2(instance_id):
    try:
        response = client.start_instances(
            InstanceIds = [instance_id]
        )
        current_state = response['StartingInstances'][0]['CurrentState']['Name']
        previous_state = response['StartingInstances'][0]['PreviousState']['Name']
        message = f'InstanceId: {instance_id} current state is {current_state} and previous state was {previous_state}'
        return message
    except:
        print('Não foi possível dar um start na instância. Tente novamente')

def get_ebs_volumes():
    try:
        volumes =[]
        response = client.describe_volumes()
        for volume in response['Volumes']:
            volume_id = volume['VolumeId']
            volume_type = volume['VolumeType']
            volume_state = volume['State']
            instance_id = volume['Attachments'][0]['InstanceId']
            instance_name = ec2_name_filter_by_id(instance_id)
            temp_dict = {}
            temp_dict['volume_id'] = volume_id
            temp_dict['volume_type'] = volume_type
            temp_dict['volume_type'] = volume_type
            temp_dict['volume_state'] = volume_state
            temp_dict['instance_id'] = instance_id
            temp_dict['instance_name'] = instance_name
            volumes.append(temp_dict)
    except:
        print('Não foi possível obter informações do EBS. Tente novamente')
    
def get_volumes_available():
    try:
        response = client.describe_volumes(
            Filters = [
                {
                    'Name': 'status',
                    'Values': [
                        'available',
                    ]
                },
            ],
        )
        count_volumes = response['Volumes']
        return len(count_volumes)
    except:
        print('Não foi possível listar os EBS. Tente novamente')

try:
    for ec2 in get_ec2_all():
        ec2_instanceid = ec2['instance_id']
        ec2_state_name = ec2['instance_state_name']
        ec2_name = ec2['instance_name']
        print(ec2_instanceid, ec2_state_name, ec2_name)
except:
    print('Não foi possível listar as vms. Tente novamente')

print(get_volumes_available())