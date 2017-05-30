#include<bits/stdc++.h>
using namespace std;

struct node {
	int val;
	int size;
	int height = 0;
	node* left;
	node* right;
};

node* make_node(int x) {
	node* n = new node();
	n->val = x;
	n->left = n->right = NULL;
	n->size = 1;
	n->height = 0;
	return n;
}

node* get_min(node* root)
{
	for (;root->left != NULL; root = root->left);
	return root;
}

bool find(node* root, int x) {
	if(root == NULL) {
		return false;
	} else if (root->val == x) {
		return true;
	} else if (x < root->val) {
		return find(root->left, x);
	} else {
		return find(root->right, x);
	}
}

int height(node* root){
  if(root == NULL){
    return 0;
  } else {
    return root->height;
  }
}

int nsize(node* root){
  if(root == NULL){
    return 0;
  } else {
    return root->size;
  }
}

int set_height(node* root){
  if (root == NULL) {
    return 0;
  }
  return 1 + max(height(root->left), height(root->right));
}

int set_size(node* root){
  if (root == NULL) {
    return 0;
  }
  return 1 + nsize(root->left) + nsize(root->right);
}

node* rot_left(node* root){
  node* r = root->right;
  root->right = root->right->left;
  r->left = root;
  root->height = set_height(root);
  root->size = set_size(root);
  r->height = set_height(r);
  r->size = set_size(r);
  return r;
}

node* rot_right(node* root){
  node* r = root->left;
  root->left = root->left->right;
  r->right = root;
  root->height = set_height(root);
  root->size = set_size(root);
  r->height = set_height(r);
  r->size = set_size(r);
  return r;
}

int diff(node* left, node* right){
  return height(left) - height(right);
}

node* insert(node* root, int x){
  if (root == NULL) {
		root = make_node(x);
	} else if (x < root->val) {
		root->left = insert(root->left, x);
	} else {
		root->right = insert(root->right, x);
	}
  int d = diff(root->left, root->right);
  if(d > 1){
    if(height(root->left->left) >= height(root->left->right)){
      root = rot_right(root);
    } else {
      root->left = rot_left(root->left);
      root = rot_right(root);
    }
  } else if (d < -1) {
    if(height(root->right->right) >= height(root->right->left)){
      root = rot_left(root);
    } else {
      root->right = rot_right(root->right);
      root = rot_left(root);
    }
  }
  root->height = set_height(root);
  root->size = set_size(root);
  return root;
}

node* del(node* root, int x) {
    if (root == NULL) return root;
    if ( x < root->val) {
      root->left = del(root->left, x);
    } else if( x > root->val) {
      root->right = del(root->right, x);
    } else {
      if (root->left == NULL && root->right == NULL) { 
			  delete root;
			  root = NULL;
		  } else if (root->left == NULL) {
			  node *temp = root;
			  root = root->right;
			  delete temp;
		  } else if (root->right == NULL) {
			  node *temp = root;
			  root = root->left;
			  delete temp;
		  } else { 
			  node *temp = get_min(root->right);
			  root->val = temp->val;
			  root->right = del(root->right,temp->val);
		  }
    }
    if (root == NULL) return root;
    int d = diff(root->left, root->right);
    if (d > 1) {
      if(height(root->left->left) >= height(root->left->right)){
        root = rot_right(root);
      } else {
        root->left = rot_left(root->left);
        root = rot_right(root);
      }
    } else if (d < -1) {
      if(height(root->right->right) >= height(root->right->left)){
        root = rot_left(root);
      } else {
        root->right = rot_right(root->right);
        root = rot_left(root);
      }
    }
    root->height = set_height(root);
    root->size = set_size(root);
    return root;
}

int at_index(node *root, int k) {
  while (root) {
    if (nsize(root->left) + 1 == k) {
      return root->val;
    } else if (k > nsize(root->left)) {
      k = k - (nsize(root->left) + 1);
      root = root->right;
    } else {
      root = root->left;
    }
  }
  return -1;
}

bool right_find(node* root, int x) {
  if (root == NULL) return false;
  if (root->val == x) return true;
  return right_find(root->right, x);
}

int index_of(node* root, int x) {
  int s = 0;
  while (root) {
    if (root->left && root->left->val == x) {
      root = root->left;
    } else if (right_find(root->left, x)) {
      s += nsize(root->left) - nsize(root->left->right);
      root = root->left->right;
    } else if (root->val == x) {
      s += nsize(root->left);
      return s;
    } else if (x < root->val) {
      root = root->left;
    } else {
      s += nsize(root->left) + 1;
      root = root->right;
    }
  }
	return -2;
}

void inorder(node *root) {
	if (root == NULL) return;
	inorder(root->left);
	printf("%i ", root->val);
	inorder(root->right);
}


int main() {
  int n, m, a;
  node* root = NULL;
  scanf("%i %i", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%i", &a);
    root = insert(root, a);
  }
  char q;
  int v, ans = 0;
  for (int i = 0; i < m; i++) {
    scanf(" %c %i", &q, &v);
    v = v ^ ans;
    if (q == 'I') {
      root = insert(root, v);
    } else if (q == 'R') {
      root = del(root, v);
    } else if (q == 'S') {
      ans = at_index(root, v);
      printf("%i\n", ans);
    } else if (q == 'L') {
      ans = index_of(root, v) + 1;
      printf("%i\n", ans);
    }
  }
  inorder(root);
}