const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Register Feature", function () {
 
  it("Success Register", async function () { 
    const response = await domain 
      .post("/register")
      .send({ email: "tesbriyanya@gmail.com", password: "tesbriyan", name: "testernya briyan" });

    expect(response.statusCode).to.eql(200);
    expect(response.body.status).to.eql('SUCCESS_REGISTER');
    expect(response.body.message).to.eql('created user!');
    expect(response.body.data).to.eql('berhasil');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });
 
  it("Gagal registrasi, sudah ada email terdaftar", async function () { 
    const response = await domain 
      .post("/register")
      .send({ email: "tes@gmail.com", password: "tes123", name: "tester ganteng" });

    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_REGISTER');
    expect(response.body.message).to.eql('Gagal Registrasi');
    expect(response.body.data).to.eql('Email sudah terdaftar, gunakan Email lain');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal registrasi, email/username/password kosong", async function () { 
    const response = await domain 
      .post("/register")
      .send({ email: "", password: "tes123", name: "tester ganteng" });

    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_REGISTER');
    expect(response.body.message).to.eql('Gagal Registrasi');
    expect(response.body.data).to.eql('Email/Username/Password tidak boleh kosong');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal registrasi, email tidak valid, harus ……@blablabla.com.", async function () { 
    const response = await domain 
      .post("/register")
      .send({ email: "tes", password: "tes123", name: "tester ganteng" });

    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_REGISTER');
    expect(response.body.message).to.eql('Cek kembali email anda');
    expect(response.body.data).to.eql('Email tidak valid');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Gagal registrasi, username/password tidak boleh mengandung simbol.", async function () { 
    const response = await domain 
      .post("/register")
      .send({ email: "tesdoangyak@gmail.com", password: "tes123#@!gm", name: "tester cakep loh" });

    expect(response.statusCode).to.eql(420);
    expect(response.body.status).to.eql('FAILED_REGISTER');
    expect(response.body.message).to.eql('Tidak boleh mengandung symbol');
    expect(response.body.data).to.eql('Nama atau password tidak valid');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

})
