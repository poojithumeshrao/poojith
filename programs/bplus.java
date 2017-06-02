class pair{
    int value;
    node next;
    
} 
class node{
    pair[] p = new pair[10];
    node parent,prev; 
    boolean leaf;
    int size;
    node(){
	size = 0;
	for(int i = 0;i<10;i++)
	    p[i]=new pair();
    }
}

public class bplus{
    final int deg = 3;
    static node start = new node();
    bplus(){
	start.leaf=true;
    }
     public static void main(String args[]){
	bplus tree = new bplus();
	//node temp = tree.search(5);
	tree.insert(start,6);
	tree.insert(start,5);
	//tree.insert(temp,7);
	//tree.insert(temp,8);
	tree.balance(start);
	tree.print();
    }
    node search(int a){
	node curNode = start;
	//	int curVal = curNode.p[0].value;
	int i=0;
	while(!curNode.leaf && i < curNode.size){
	    if(a<curNode.p[0].value){
		curNode = curNode.prev;
		i=0;
		continue;
	    }
	        
	    else if(a<curNode.p[i].value){
		curNode = curNode.p[i-1].next;
		i=0;
		continue;
	    }
	    else if(i==curNode.size-1){
		curNode = curNode.p[i].next;
		i=0;
		continue;
	    }
	    i++;
	}
	if(!curNode.leaf){
	    System.out.println("error in leaf node");
	    System.exit(0);
	    return curNode;
	}
	else
	    return curNode;
    }
    void balance(node a){
	int flag =0;
	if(a.size<deg){
	    System.out.println("no need in balancing");
	    return;
	    
	}
	else{
	    node tempParent = new node();
	    if(a.parent == null){
		flag =1;
		a.parent = tempParent;
		this.start=tempParent;
		tempParent.prev = a;
		tempParent.p[0].value=a.p[a.size/2].value;
		tempParent.leaf = false;
	    }
	    node temp = new node();
	    if(flag ==1){
		    tempParent.p[0].next=temp;
	    }
	    temp.parent = a.parent;
	    temp.leaf = true;
	    int i,j;
	    for(i=a.size/2,j=0;i< a.size;i++,j++){
		temp.p[j]=a.p[i];
	    }
	    temp.size = a.size-a.size/2;
	    a.size = a.size/2;
	}
    }

    void insert(node a,int val){
	if(!a.leaf)
	    System.out.println("error in calling insert");
	int temp,temp2;
	int i;
	//System.out.println(a.size);
	for(i=0;i<a.size;i++){
	    //   System.out.println(a.p[i].value);
	    if(a.p[i].value>val){
		
		break;
	    }
	}
	a.p[i].value=val;
	for(int j= a.size;j>i;j--)
	    a.p[j].value = a.p[j-1].value;
	a.size++;
    }
    void print(){
	node curNode=start;
	while(true){
	    if(!curNode.leaf)
		curNode=curNode.prev;
	    else
		break;
	}
	while(true){
	    for(int i=0;i<curNode.size;i++)
		System.out.println(curNode.p[i].value);
	    curNode = curNode.p[curNode.size-1].next;
	    if(curNode==null)
		break;
	}
    }
   
}
        

        
    
        

