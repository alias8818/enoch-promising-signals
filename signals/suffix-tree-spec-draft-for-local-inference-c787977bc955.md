# Suffix-Tree Spec Draft for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-spec-draft-for-local-inference-c787977bc955`
Run ID: `suffix-tree-spec-draft-for-local-inference-c787977bc955-20260603T200200984508+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c067134b618a

## What looked useful

Suffix-context drafting produced substantially higher accepted-token yield than fixed trigram and bigram controls on repetitive local text (3.078 accepted tokens per 4-token proposal on service logs) and a smaller gain on code-like stdlib text (0.604 versus 0.382 trigram), while collapsing on random noise. This supports the mechanism only for repetition-heavy local inference workloads.

## Boundaries and scale limits

No integrated transformer decoding, no KV-cache or verifier timing, no neural target distribution, no quality measurement, and no production memory-optimized implementation. Largest confirmation used 50k held-out positions per eligible corpus and a 1.5 MB stdlib slice.

## Claim scope

Offline acceptance-proxy evaluation of a reversed suffix-context draft index on local repetitive logs, Python stdlib text, controller prompt text, and random-noise control with draft length 4 and max suffix context 16.

## Why it stopped

Proxy/offline acceptance evidence is useful but insufficient for a paper-positive inference claim; it does not validate end-to-end local LLM speedup.

## Recommended next action

Stop this run as a no-paper useful-signal proxy result; the one concrete next action is a bounded local transformer decoding integration that measures end-to-end tokens/s and target forward-pass reduction on repetitive prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrate suffix-context drafting into local transformer speculative decoding
- Success threshold: At least 10% end-to-end tokens/s improvement over no drafting and at least 5% over fixed n-gram control on repetition-heavy prompts, with no material degradation in generated output checks and no more than 2 GB additional peak memory for the compact index.
- Stop condition: Stop if suffix-context drafting fails to improve end-to-end tokens/s on repetition-heavy prompts, if verifier overhead exceeds accepted-token savings, or if memory growth cannot be bounded below the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-spec-draft-for-local-inference-c787977bc955`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
