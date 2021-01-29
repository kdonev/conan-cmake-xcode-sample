import SwiftUI

struct ContentView: View {
    var body: some View {
        Text( String(cString: zmqConnectVersion()) )
            .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
