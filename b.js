async function sendRequest() {
    const url = "https://kanal.umk.ac.id/mahasiswa/entrirencanastudi";
    const headers = {
      "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "accept-language": "en-US,en;q=0.9,id;q=0.8,it-IT;q=0.7,it;q=0.6",
      "cache-control": "max-age=0",
      "content-type": "application/x-www-form-urlencoded",
      "priority": "u=0, i",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "document",
      "sec-fetch-mode": "navigate",
      "sec-fetch-site": "same-origin",
      "sec-fetch-user": "?1",
      "upgrade-insecure-requests": "1"
    };
    const body = "_token=CFFnTbMWpTGXEp8q8klzYEjrPE0HGAgEPnqsDqwf&makul%5B%5D=NDYzNzA5MzMyNzExMjc0N2JmOTg1NDY4N2I4ZDBhYzhkNGIzN2EyY2QzNjc0MzM3ZWZiZTE3MzFkODAxNGM5OGQxMDhjZmVmYTlhZmJmMmQxYjYyNmExODRiZjgyZjRiMzcyOWYxNjc4ZDk4NWQ0NThhN2I3MTRkMzExOGFhNTUzOHRHV2dzZXdySnJkY0I4OHkyOUcydlRhTU12bWM5NCtCREhDRXFSSzJZPQ&makul%5B%5D=ODMxNTA5OWJmNjM0ZTMyMTU3OTQ1YmZiYWQ2ODQyOTc5NzgyODUxNTczODYzZDcyODA4YjZkODY2YzI5Nzc3NGRkMTc4NDMyZWM0ZmU1OTExZTY0MmJjOTZkNzFhODNlNDE4MmFkZjFmZTNjNDE4ZDYxNmJjYzNlY2NmNTc0MDFoSFhGRjhiVEJIV3JodVR3cWthSmtVRXVuc0lGcVpSV0VNMnpsQlhYMFlvPQ&makul%5B%5D=MjI3MTc2YjEwYTIyYTU5M2IyNDkxYTA2OWQzNDdhZTNjMzJlMzc1MDViOWIzMDI3NjZhZWZkMDQzNGRkYjQzNzZiYjBiZjYwNTBlY2FlZDZjYmQ2MDBiZjQ2YTc4ZjYzNGJmMzRkMjQ1MzFmMzk0NzVhNDBhMjQ5MTk4ZTJmMWZiY0gxMlUzZENhYWQvWnIxc0JXdW05TTJxU25XWXdPUjYzaUEzb2ZHZ2VrPQ&makul%5B%5D=Nzc2MjVjMWYwNTcwYmRiOTNiNjVhOTc0YjA0ZDhhMjZlODU4MzI4NzY5YjA4MTYzOTU3ZDZhZGI2YzgwOTk0MTQwNmY3NTg0MDgyZjU3MDc4MTBhYzk3YTNjNWNlYmE0OTVmMjBiYWY4NDExODk0NzJiODI5ZjlmNjg1ODI2MTNQS2dvNzd6VXpUaDdPNTZpbmg3Y0RldnVQL3o4NllGbGVDcEZUaklzeSswPQ&makul%5B%5D=NTJkOGRjZGUxNzhmYzgxY2VkNDA2OTZkMmFlMjdhY2VhNzk3NmQyYjNjNGNiN2I2YTNhMmE1OTMyMWJkY2RmNWViM2E0MjNlMjZmZjc5NTQ3MTU1NDE1MGZmMDliNTA0ZmE1YjhjMDQ3YmNhNDlmY2IxMjI1NTBjM2U5Mzg5YWFFQy8wS1ZURmZKV202b1VzdkpCbUZ0d3oyeGhGV0lZd0EwWVBsREFFNHQ0PQ&submit=";
  
    function showLoading() {
      const loadingChars = ['|', '/', '-', '\\'];
      let i = 0;
      const intervalId = setInterval(() => {
        process.stdout.write(`\rLoading ${loadingChars[i]}`);
        i = (i + 1) % loadingChars.length;
      }, 100);
      return intervalId;
    }
  
    async function makeRequest() {
      const loadingInterval = showLoading();
      try {
        const response = await fetch(url, {
          headers: headers,
          referrer: "https://kanal.umk.ac.id/mahasiswa/entrirencanastudi",
          referrerPolicy: "strict-origin-when-cross-origin",
          body: body,
          method: "POST",
          mode: "cors",
          credentials: "include"
        });
        clearInterval(loadingInterval);
        console.log('\rDone!     \n');
        console.log("Status Code:", response.status);
        const responseText = await response.text();
        console.log("Response:", responseText);
        setTimeout(makeRequest, 5000); 
      } catch (error) {
        clearInterval(loadingInterval);
        console.log('\rError!     \n');
        console.error("Error:", error);
        setTimeout(makeRequest, 5000); 
      }
    }
  
    makeRequest();
  }
  
sendRequest();