#include <Windows.h>
#include <GL/gl.h>

typedef void (APIENTRY* glDrawElements_t)(GLenum mode, GLsizei count, GLenum type, const void* indices);
glDrawElements_t o_glDrawElements = nullptr; 

// Hooks
void APIENTRY hk_glDrawElements(GLenum mode, GLsizei count, GLenum type, const void* indices) {
    o_glDrawElements(mode, count, type, indices);
}

void HookOpenGL() {
    o_glDrawElements = (glDrawElements_t)wglGetProcAddress("glDrawElements");
    DetourFunction((PBYTE)o_glDrawElements, (PBYTE)hk_glDrawElements);
}

// Dll
DWORD WINAPI MainThread(HMODULE hModule) {
    HookOpenGL();
    return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        CreateThread(nullptr, 0, (LPTHREAD_START_ROUTINE)MainThread, hModule, 0, nullptr);
    }
    return TRUE;
}