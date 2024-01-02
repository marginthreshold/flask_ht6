import uvicorn

if __name__ == '__main__':
    uvicorn.run('main2:app', port=80, reload=True)
