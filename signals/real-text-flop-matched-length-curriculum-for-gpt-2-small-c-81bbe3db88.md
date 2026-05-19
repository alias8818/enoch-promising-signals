# Real-text FLOP-matched length curriculum for GPT-2-small-class training

Status: `useful_signal`
Project ID: `real-text-flop-matched-length-curriculum-for-gpt-2-small-c-81bbe3db88`
Run ID: `real-text-flop-matched-length-curriculum-for-gpt-2-small-c-81bbe3db88-20260517T000804810045+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a610f7413d8

## What looked useful

Curriculum improved validation loss in all three paired seeds; mean delta was -0.03122 nats and mean perplexity was about 3.07% lower at matched estimated FLOPs.

## Boundaries and scale limits

Not validated at GPT-2 small 124M parameters, 1024-token context, WebText/OpenWebText scale, long-horizon convergence, or broad schedule/optimizer sweeps.

## Claim scope

In a Tier 1 direct Wikitext-2 experiment with a 29.995M parameter GPT-2-style decoder, 128-token target context, three paired seeds, and matched estimated training FLOPs, a 32->64->128 length curriculum reduced held-out 128-token next-token loss versus constant 128-token training.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains too small and narrow for a paper; this is no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a medium confirmation with a larger GPT-2-style model or 124M-class configuration, 512-token or longer contexts, a token-matched control, and at least 5 paired seeds before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of FLOP-matched length curriculum with longer contexts
- Success threshold: Curriculum beats constant-length baseline by at least 0.02 nats mean validation loss at final context length, with improvement in at least 4 of 5 paired seeds and no worse last-quarter position-bucket loss.
- Stop condition: Stop as negative if the curriculum fails to improve mean final-context validation loss by 0.01 nats or if gains disappear under the token-matched control.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-flop-matched-length-curriculum-for-gpt-2-small-c-81bbe3db88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
