const RemoteRunnable = require("@langchain/core/runnables/remote").RemoteRunnable;

async function run() {
    const remoteChain = new RemoteRunnable({
    url: "http://localhost:8000/",
    });

    const result = await remoteChain.invoke("water");

    console.log(result);

    const stream = await remoteChain.stream("tree");

    for await (const chunk of stream) {
      console.log(chunk);
    }
}
run().then(() => console.log("done")).catch(console.error);
