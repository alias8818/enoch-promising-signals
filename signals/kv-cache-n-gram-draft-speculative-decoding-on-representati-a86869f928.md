# KV-cache n-gram draft speculative decoding on representative corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-draft-speculative-decoding-on-representati-a86869f928`
Run ID: `kv-cache-n-gram-draft-speculative-decoding-on-representati-a86869f928-20260522T141804390909+0000`

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

- Parent run decision: N-Gram Draft Speculative Decoding: enoch://control-plane/projects/n-gram-draft-speculative-decoding-0acad1cfb114/runs/n-gram-draft-speculative-decoding-0acad1cfb114-20260522T135735156917+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

The mechanism is plausible in bounded local evidence: n-gram proposals are common and often accepted by a small target LM, with strongest gains on repeated code and moderate gains on wiki-like prose. Longer n-grams improved acceptance over n=1, but part of the effect is simple recency/frequency.

## Boundaries and scale limits

No actual speculative decode loop, persistent target KV-cache timing, multi-token generated-context verification, larger target model, serving kernel benchmark, or broad corpus sweep was run. Shakespeare-style prose stayed below the 1.20x per-domain target-call reduction threshold.

## Claim scope

Tier 1 small direct test: online exact n-gram cache proposals on three real text corpora, verified against distilgpt2 greedy next-token predictions, produced mean proposal coverage 0.827 and conservative one-token target-call reduction estimate 1.443x.

## Why it stopped

No-paper closure: Tier 1 evidence supports the mechanism but remains a small direct acceptance test and conservative speed proxy, not a publication-grade decoding benchmark.

## Recommended next action

Run a bounded deepen follow-up implementing an actual speculative decode loop with persistent KV-cache and multi-token drafts, comparing wall-clock tokens/sec against a no-draft baseline on distilgpt2 or gpt2 across the same corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock KV-cache n-gram speculative decode loop on small pretrained LMs
- Success threshold: At least 1.15x wall-clock tokens/sec improvement over no-draft greedy decoding on the mean corpus mixture, with no corpus below 0.95x and exact greedy-output equivalence.
- Stop condition: Stop as negative if the actual decode loop is slower than baseline on the mean mixture or if gains appear only on the repeated code corpus while both natural-language corpora remain below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-draft-speculative-decoding-on-representati-a86869f928`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
