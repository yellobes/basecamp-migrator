#! /bin/bash


#      [] [] [] []    [] [] [] []    []         []

#      []                      []     []        []

#      [] [] [] []        []         []    []   []

#               []             []    []        []

#      [] [] [] []    [] [] [] []    []         []

#    Binarysprocket 2012



ac_url='192.168.1.8'
path='/activecollab'
token='1-4vsy76QCTaKpnzoJhvCKvhpFhw8pz8hVpFQjli4'

project_name=
project_leader_id=



curl -d "submitted=submitted&project[name]=$project_name&project[leader_id]=$project_leader_id" "$ac_url$path/public/api.php?path_info=/projects/add&token=$token"




