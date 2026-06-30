# N-gram speculative decode for GPT-2-small on CPU+GPU 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decode-for-gpt-2-small-on-cpu-gpu-10gb-01e78baef6ea`
Run ID: `n-gram-speculative-decode-for-gpt-2-small-on-cpu-gpu-10gb-01e78baef6ea-20260528T043944602985+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fb138a1f701a

## What looked useful

Fp32 exact speculative decoding matched baseline tokens across all tested prompts. Draft length 8 gave 1.97x mean and 1.23x median speedup across all prompts, but natural prompts only reached 1.08x mean and 1.05x median while repetitive prompts reached 3.75x mean and 3.84x median. Default fp16 runs diverged from baseline output by 96 tokens on prompt 0 for draft lengths 2, 4, and 8.

## Boundaries and scale limits

Only 12 prompts and 96 generated tokens per prompt were tested; four prompts were intentionally repetitive; no production serving stack, batching, sampling, fp16-safe exactness, or large corpus evaluation was validated.

## Claim scope

On NVIDIA GB10 with GPT-2-small greedy decoding, a CPU n-gram proposer plus GPU fp32 batched verification can exactly match baseline greedy output and improve throughput mainly on repetitive prompts; natural-prompt gains are small and inconsistent in this local 12-prompt benchmark.

## Why it stopped

No-paper useful signal: the local fp32 mechanism works, but natural-prompt gains are mixed, fp16 exactness failed, and the prompt set is too small for a publication-grade claim.

## Recommended next action

Run a bounded deepen follow-up that either makes fp16 verification exact or scopes the method to fp32, then evaluates at least 100 natural prompts plus a separated repetition subset with exact output equality and median natural-prompt speedup >= 1.10x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fp16-safe and corpus-scale n-gram speculative decoding for GPT-2-small
- Success threshold: Exact outputs on all prompts and median natural-prompt throughput speedup >= 1.10x with no more than 5% natural prompts slower than baseline by more than 10%.
- Stop condition: Stop if fp16 exactness cannot be achieved or if the larger natural-prompt benchmark has median speedup <= 1.00x for all draft lengths.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decode-for-gpt-2-small-on-cpu-gpu-10gb-01e78baef6ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
