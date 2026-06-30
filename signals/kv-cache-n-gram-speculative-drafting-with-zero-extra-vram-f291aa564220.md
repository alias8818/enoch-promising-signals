# KV-Cache N-Gram Speculative Drafting with Zero Extra VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculative-drafting-with-zero-extra-vram-f291aa564220`
Run ID: `kv-cache-n-gram-speculative-drafting-with-zero-extra-vram-f291aa564220-20260529T194043245024+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ec37227404fd

## What looked useful

History-only n-gram drafting creates negligible useful acceleration on ordinary prose-like and sampled tiny-model traces. Best target-call reduction was 1.0666x, but measured verifier chunk costs reduced the best projected wall-clock speedup to 1.0007x; sampled model traces had effectively no reusable drafts.

## Boundaries and scale limits

No 7B+ model, no production serving stack, no batching study, no long-context/code-domain workload, and no custom verifier kernel. Results should be read as an early falsification of broad/general usefulness, not a full impossibility proof.

## Claim scope

Bounded local probe of assistant-model-free n-gram speculative drafting using prior token history on 71 prose-like token traces, 4 tiny-GPT-2 sampled continuations, and cached tiny-GPT-2 verifier chunk timing on GB10.

## Why it stopped

Proxy/local evidence is an early falsification of the general zero-extra-VRAM n-gram drafting claim: reusable drafts are too rare on tested traces and verifier chunk overhead erases the small target-call reduction.

## Recommended next action

Stop this broad variant as no-paper evidence; only revisit with a domain-gated code/template workload where repeated suffixes are common and the success threshold is end-to-end tokens/sec, not target-call count.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Domain-Gated N-Gram Drafting for Repetition-Heavy Code and Template Generation
- Success threshold: At least 5% end-to-end tokens/sec improvement with p50 and p95 latency not worse than baseline by more than 2%, GPU memory overhead below 1%, and identical deterministic outputs or statistically unchanged sampling quality.
- Stop condition: Stop if gated drafting accepts below 0.15 draft tokens per verifier call, dead/no-draft calls exceed 90%, or measured end-to-end speedup is below 2% on the first 20k emitted tokens.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculative-drafting-with-zero-extra-vram-f291aa564220`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
