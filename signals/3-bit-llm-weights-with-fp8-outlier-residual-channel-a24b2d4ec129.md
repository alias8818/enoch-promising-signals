# 3-bit LLM weights with FP8 outlier residual channel

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `3-bit-llm-weights-with-fp8-outlier-residual-channel-a24b2d4ec129`
Run ID: `3-bit-llm-weights-with-fp8-outlier-residual-channel-a24b2d4ec129-20260614T115452225083+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/961265193d4e

## What looked useful

At comparable storage, int3+FP8 residual 12.5% columns used about 4.126 estimated bpw and had weighted output NMSE 0.014521, while int4 used about 4.125 estimated bpw and had weighted output NMSE 0.004554. The residual scheme improved int3 by 45.5% but remained 3.19x worse than int4; even 50% residual columns at about 7.13 bpw remained 1.30x worse than int4.

## Boundaries and scale limits

Tested 24 GPT-2-class Conv1D layers, 2048 activation rows per layer, group size 128, dequantized layer-output error only. Did not test end-to-end perplexity, packed inference kernels, generation quality, or 7B+ models.

## Claim scope

On distilgpt2 projection and MLP weights with WikiText-2 activation samples, symmetric groupwise int3 plus FP8 residual input columns reduces int3 layer-output error but is not competitive with symmetric groupwise int4 at comparable estimated bits per weight.

## Why it stopped

Proxy/local early falsification: the directly tested mechanism improves int3 but fails the matched-budget int4 layer-output-error baseline by a large margin.

## Recommended next action

Stop this line as a paper candidate unless a future end-to-end quantized perplexity test with a packed implementation demonstrates an advantage over int4 at comparable total bits per weight.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/3-bit-llm-weights-with-fp8-outlier-residual-channel-a24b2d4ec129`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
