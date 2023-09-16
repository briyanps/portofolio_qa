const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Login Feature", function () {
  it("Sukses login,data user tersimpan di DB.", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "tes@gmail.com", password: "tes123"});

    expect(response.statusCode).to.eql(200);
    expect(response.body.status).to.eql('SUCCESS_LOGIN');
    expect(response.body.message).to.eql('Anda Berhasil Login');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, data tidak ditemukan di DB.", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "tes@gmail.com", password: "tes12345"});
    
    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email atau Password Anda Salah');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, email tidak valid", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "test", password: "tes12345"});
   
    expect(response.statusCode).to.eql(420);  
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Cek kembali email anda');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, email dikosongkan", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "", password: "tes12345"});
   
    expect(response.statusCode).to.eql(420);  
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email tidak boleh kosong');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, password dikosongkan", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "tes@gmail.com", password: ""});
    
    expect(response.statusCode).to.eql(420);    
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Password tidak boleh kosong');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, email dan password dikosongkan", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "", password: ""});
    
    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email & Password tidak boleh kosong');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, email lebih dari 50 karakter", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "tes123456789123456789123456789123456789123456789@gmail.com", password: "tes123"});
    
    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email/Password melebihin maksimal karakter');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal login, password lebih dari 20 karakter", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "tes@gmail.com", password: "tes123345678912345678912"});
    
    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email/Password melebihin maksimal karakter');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

});