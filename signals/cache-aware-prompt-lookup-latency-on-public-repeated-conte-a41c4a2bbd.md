# Cache-aware prompt-lookup latency on public repeated-context prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cache-aware-prompt-lookup-latency-on-public-repeated-conte-a41c4a2bbd`
Run ID: `cache-aware-prompt-lookup-latency-on-public-repeated-conte-a41c4a2bbd-20260531T101640909070+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Prompt-Lookup N-gram Speculative Decoding: enoch://control-plane/projects/prompt-lookup-n-gram-speculative-decoding-8f6de0dd92f4/runs/prompt-lookup-n-gram-speculative-decoding-8f6de0dd92f4-20260530T052251096655+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

On distilgpt2, prompt_lookup_num_tokens=5 improved median latency by 1.80x on Alice and 1.40x on Gettysburg when generated output overlapped the prompt, reducing forward calls from 32 to 8-9. On Declaration, where generated output did not overlap the prompt, prompt lookup had no forward-call reduction and slowed to 0.60x of baseline. The result supports a conditional mechanism, not a broad paper claim.

## Boundaries and scale limits

Single model, CPU-only, 4 iterations per prompt, 32-token greedy generation, hand-crafted prompts, no production serving stack, no GPU/KV-cache serving comparison, no larger instruction-tuned models, and one speedup case had a one-token output mismatch.

## Claim scope

Small CPU direct test of Hugging Face Transformers prompt lookup decoding on distilgpt2 with hand-constructed public-domain repeated-context prompts. Prompt lookup reduced latency when generated continuations had high prompt n-gram overlap, but repeated context alone was not sufficient and one repeated public prompt slowed down.

## Why it stopped

Tier 1 controlled direct test completed and produced a mixed useful signal, but evidence is too narrow and partly confounded for publication readiness.

## Recommended next action

Run a bounded medium confirmation that stratifies public prompts by measured generated-output prompt-overlap across at least two more small/medium causal LMs, with exact-output checks and per-token latency normalization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt lookup latency by generated-copy overlap across small open LMs
- Success threshold: Across at least two of three models, high-overlap prompts show >=1.25x median per-token latency speedup with no semantic/output regression, while low-overlap prompts show <=1.05x speedup or slowdown, confirming the conditional mechanism.
- Stop condition: Stop if high-overlap prompts fail to reach 1.15x median speedup on two models, if output mismatches are common enough to prevent same-output comparisons, or if runtime exceeds the local CPU budget without producing at least 20 prompts per stratum.

## Evidence references

- Artifact root: `<local-path>/projects/cache-aware-prompt-lookup-latency-on-public-repeated-conte-a41c4a2bbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
