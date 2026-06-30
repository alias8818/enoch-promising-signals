# CPU N-Gram Speculative Draft for GPT-2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cpu-n-gram-speculative-draft-for-gpt-2-de153675b691`
Run ID: `cpu-n-gram-speculative-draft-for-gpt-2-de153675b691-20260523T221846042914+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4550ade894df

## What looked useful

Exact CPU n-gram speculative verification is easy to implement for GPT-2, but the tested drafter had low acceptance and increased target-model forwards. GPT-2 small wall-time speedup was 0.83x to 0.84x on the 12-prompt runs, so the mechanism was slower than cached greedy decoding in this bounded setting.

## Boundaries and scale limits

This run tested GPT-2 small only, greedy decoding only, 12 manually chosen prompts, 32 generated tokens per prompt, and a simple history-copy n-gram drafter. It did not test long-context corpora, batched serving, sampling, GPU verification, or a trained draft model.

## Claim scope

On 12 short open-ended prompts with GPT-2 small greedy decoding for 32 new tokens each, a history-copy n-gram CPU drafter with exact cached verification preserved greedy outputs but did not accelerate decoding.

## Why it stopped

Direct bounded GPT-2 small tests showed exactness but slower decoding and no forward reduction; this is a practical early falsification of the acceleration claim, not a full validation across all workloads.

## Recommended next action

Stop this line as a no-paper negative unless a future project changes the drafter objective or workload; do not scale the same history-copy n-gram scheme as tested here.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-draft-for-gpt-2-de153675b691`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
