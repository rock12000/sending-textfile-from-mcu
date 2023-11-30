include reg51.h 
void SerTx(unsigned char);  
void main(void)  
{  
  TMOD = 0x20;  
  TH1 = 0xFD;  
  SCON = 0x50;  
  TR1 = 1;  

FILE* ptr;
    char ch;
 
    // Opening file in reading mode
    ptr = fopen("sample.txt", "r");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    // Sending what is written in file
    // character by character using loop.
    do {
        ch = fgetc(ptr);
        printf("%c", ch);
	SerTx("%c", ch);
    } while (ch != EOF);

// Closing the file
    fclose(ptr);
    return 0; 

}

void SerTx(unsigned char x)  
{  
  SBUF = x;  
  while(TI==0);   
  TI = 0;   
}  