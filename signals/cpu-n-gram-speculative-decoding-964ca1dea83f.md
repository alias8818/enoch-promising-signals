# CPU N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-964ca1dea83f`
Run ID: `cpu-n-gram-speculative-decoding-964ca1dea83f-20260525T045930973359+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fbfbc972dd11

## What looked useful

CPU overhead was low relative to plausible target-model verification cost: best word trained n-gram p95 lookup was 6.993 us with 0.082 ms break-even target-call latency, and best byte trained n-gram p95 lookup was 55.624 us with 0.044 ms break-even latency. The mechanism is plausible, but only as a bounded trace result.

## Boundaries and scale limits

No actual transformer logits, BPE tokenizer, KV-cache verification, sampling behavior, production prompts, or end-to-end LLM serving wall-clock measurement were tested. Corpora were small and public; byte-token results likely overstate production LLM-token performance.

## Claim scope

Dependency-free trace replay on two small public text corpora shows that CPU trained n-gram drafters can reduce oracle target verification calls by 3.05% median and 5.70% max on word tokens, and by 30.93% median and 37.80% max on byte tokens; prompt-lookup alone is near-zero on word tokens but modestly useful on byte tokens.

## Why it stopped

Trace replay supports a mechanism but is not full validation; prompt-lookup is effectively negative on word-token traces and trained n-gram gains need direct model-serving evidence before any paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should directly test a BPE-tokenized GPT-2-small-class CPU decoding loop with real batched speculative verification and compare end-to-end wall-clock speed against baseline greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE and Small-Model CPU Validation for N-Gram Speculative Decoding
- Success threshold: At least 10% end-to-end tokens/s improvement over baseline greedy decoding on a held-out prompt set, with no more than 5% degradation in exact greedy output agreement under deterministic decoding.
- Stop condition: Stop as negative if BPE trace replay or direct small-model decoding shows under 5% target-call reduction or no positive wall-clock speedup after CPU draft overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-964ca1dea83f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
