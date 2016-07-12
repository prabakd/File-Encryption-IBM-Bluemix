import base64
import os,sys
import swiftclient.client as swiftclient


#### Variables for connection to IBM Bluemix Replace XXXX with your environment variables.
auth_url = 'https://identity.open.softlayer.com'+'/v3'
project_name = 'XXXXXX'
password = 'XXXXXXX'
user_domain_name = 'XXXXX'
project_id = 'XXXXXX'
user_id ='XXXXXX'
region_name ='XXXXX'

# Get a Swift client connection object
conn = swiftclient.Connection(
        key=password,
        authurl=auth_url,
        auth_version='3',
        os_options={"project_id": project_id,
                    "user_id": user_id,
                    "region_name": region_name})

#### Variables
container_name = 'new-container'
file_name = 'example1.txt'
en_file='example1_enc.txt'
downloadedfile='example1_downnload.txt'
tmp="tmp.txt"
#### Check the file size
def check():
    total_size=0
    file_size=os.path.getsize(file_name)
    file_size=file_size/2048

    for container in conn.get_account()[1]:
        for data in conn.get_container(container['name'])[1]:
            #print 'object: {0}\t size: {1}\t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])
            if en_file == data['name']:
                return 4
            total_size = total_size + data['bytes']
    total_size=total_size/2048
    file_size_after=file_size+total_size
    if file_size < 1:
        if file_size_after < 10:
            return 1
        else:
            return 2
    else:
        return 3

##Create a new container
def upload():
    conn.put_container(container_name)
    print "\nContainer %s created successfully." % container_name

    # List your containers
    print ("\nContainer List:")
    for container in conn.get_account()[1]:
        print container['name']
    file_content = open(file_name,"rb").read()
    en_contents = base64.b64encode(file_content)
    print "Contents:"
    print en_contents
    conn.put_object(container_name,en_file,contents=en_contents)
    print "File has been uploaded successfully to the container"
   
### Download the file
def download():
    d_file=conn.get_object(container_name,en_file)
    file=open(tmp,'w')
    file.write(d_file[1])
    file.close()
    d_contents=open(tmp,'rb').read()
    print d_contents
    decrypted_data=d_contents.decode('base64')
    print decrypted_data
    file=open(downloadedfile,'w')
    file.write(str(decrypted_data))
    file.close()
    os.remove(tmp)
    print "\n File has been downloaded successfully"

# List objects in a container, and prints out each object name, the file size, and last modified date
def list_files():
    sum=0
    print ("\nObject List:")
    for container in conn.get_account()[1]:
        for data in conn.get_container(container['name'])[1]:
            print 'object: {0}\t size: {1}\t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])
            sum=sum+data['bytes']
    print sum

# Delete the object
def delete():
    conn.delete_object(container_name,en_file)
    print '{0} file deleted from container'.format(en_file)


### Main Function
choice=int(raw_input("Enter your choice \n1.Upload \n2.List Files \n3.download \n4.delete"))

if choice == 1:
   upload()
elif choice == 2:
    list_files()
elif choice == 3:
    download()
elif choice == 4:
    delete()
else:
    print "Enter your choice correctly"
