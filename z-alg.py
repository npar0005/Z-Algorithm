def get_z_array(txt):
    txt = f'#{txt}'
    n = len(txt)  # txt = #str (so txt[1] is first character of the text)
    z = [0] * n
    z[0] = None  # never used (index 0 is irrelevant)
    z[1] = n - 1  # Z(1) is the entire string, so also irrelevant

    # left and right bounds of the rightmost z-box from position `k`
    l = 0
    r = 0

    for k in range(2, n):
        # case 1: the current character is outside of the z-box (to the right of it) - also handles base case
        if k > r:
            # Perform explicit comparisons
            for i in range(k, n):
                char = txt[(i - k) + 1]  # get the character relative to k from the start of the string
                if char == txt[i]:
                    z[k] += 1
                else:
                    break

            if z[k] > 0:  # z-box was found, so we can mark it by setting l and r
                r = (k + z[k]) - 1
                l = k

        # case 2: the current character at position `k` is inside (or on the bounds of) the z-box
        elif k <= r:
            beta = (r - k) + 1  # the length of the box from the current char to the end of the z-box (defined by z[l])
            k_p = (k - l) + 1  # the mirrored position of k but at the start of the string (k')

            # case 2a: z[k'] < |beta|
            if z[k_p] < beta:  # the prefix at z[k'] is within the bounds of the beta-box, so, z[k] must equal z[k']
                z[k] = z[k_p]

            # case 2b: z[k'] >= |beta|
            elif z[k_p] >= beta:  # the prefix z[k_p] either extends the bounds of matches the bounds of the beta box
                # in this case, it is guaranteed that z[k] is at least |beta|, but it may be longer.
                # so we need to check if the characters outside the beta box (r+1 etc) match those of the prefix
                q = r + 1  # position of potential mismatch

                while q < n:
                    char = txt[beta + (q - r)]  # char at the prefix relative to r+1
                    if char == txt[q]:
                        q += 1
                    else:
                        break

                z[k] = q - k  # the region including beta + additional characters up to q
                r = q - 1
                l = k

    return z[1:]

txt = "cabacaacab"
z_array = get_z_array(txt)
print(z_array)
