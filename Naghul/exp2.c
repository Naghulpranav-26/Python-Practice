#include<stdio.h>
#include<stdlib.h>
struct node {
int data;
struct node*next;
};
struct node*start=NULL;
void insert_at_begin(int);
void insert_at_end(int);
void insert_nextto(int,int);
void delete_from_begin();
void delete_from_end();
void traversen();
int count=0;
int main(){
int d,data,i;
for(;;){
    printf("1.Insert at begin:\n");
    printf("2.Insert at end:\n");
    printf("3.Insert at next to:\n");
    printf("4.Traversen of LL:\n");
    printf("5.delete at begin:\n");
    printf("6.Delete at end:\n");
    printf("7.Exit\n");
    printf("Enter the option:\n");
    scanf("%d",&i);
    if(i==1){
        printf("Enter the element:\n");
        scanf("%d",&data);
        insert_at_begin(data);
    }
    else if(i==2){
        printf("Enter the element:\n");
        scanf("%d",&data);
        insert_at_end(data);
    }
    else if(i==3){
        printf("Enter the element after which to be inserted and enter the element:\n");
        scanf("%d %d",&d,&data);
        insert_nextto(d,data);
    }
    else if(i==4){
        traversen();
    }
    else if(i==5){
        delete_from_begin();

    }
    else if(i==6){
        delete_from_end();
    }
    else if(i==7){
        break;

    }
    else{
        print("Please Enter the valid input:\n");
    }
    return 0;
}
void insert_next_to(int x,int d){
struct node*t*temp;
t=(struct node*) malloc(size of(struct node));
t->data=x;
count++;
temp=start;
for(temp=start;temp=Null;temp=temp->next){
    if(temp->data=d){
        break;
    }
    t->next=temp->next;
    temp->next=t;
}
}
void insert_at_begin(int x);
{struct node*t;
t=(struct node*) malloc(size of(struct node));
t->data=x;
count++;
if(start==Null){
    start=t;
    start->next=Null;
    return ;
}
t->next=start;
start=t;
}
void insert_at_end(int x);
{struct node*t*temp;
t=(struct node*) malloc(size of(struct node));
t->data=x;
count++;
if(start==Null){
    start=t;
    start->next=Null;
    return ;
}
temp=start;
while(temp->next!=Null){
    temp=temp->next;
    temp->next=t;
    t->next=Null;
}
}
void traversen(){
struct node*t;
t=start;
if(t==Null){
    printf("Linked List empty \n");
    return ;
}
printf("There are %d elements in linked list:\n",count);
while(t->next!=null){
    printf("%d",t->data);
    t=t->next;
}
printf("%d",t->data);
}
void delete_from_begin(){
struct node*t;
int n;
if(start==Null){
    printf("The Linked List is Empty\n");
    return;
}
n-start->data;
t=start->next;
free(start);
start=t;
count--;
printf("%d Delete from the beginig is sucessfull:\n",n);
}
void delete_from_end(){
struct node*t*u;
int n;
if(start==Null){
    printf("The Linked List is Empty\n");
    return;
}
count--;
if(start->next==Null){
    n=start->data;
    free(start);
    start=Null;
    printf("%d Deletion is sucessfull:\n",n);
    return ;
}
t=start;
while(t->next!=Null)
{
    u=t;
    t=t->next;
}
n=t->data;
u->next=Null;
free(t);
printf("The deletion is sucess\n",n)
}
}


