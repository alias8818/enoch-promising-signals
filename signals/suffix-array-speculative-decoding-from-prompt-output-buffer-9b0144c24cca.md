# Suffix-array speculative decoding from prompt+output buffer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-from-prompt-output-buffer-9b0144c24cca`
Run ID: `suffix-array-speculative-decoding-from-prompt-output-buffer-9b0144c24cca-20260529T094113345968+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/38987278d1af

## What looked useful

Suffix arrays are a plausible compact retrieval structure for prompt lookup, but this bounded replay found only 0.09-0.79 accepted bytes/position for min_match=8 and 0.46-1.48 for min_match=4, which is too weak for a paper claim without workload-specific repetition or end-to-end model evidence.

## Boundaries and scale limits

Proxy-only byte-level corpus replay; no BPE tokenizer, no target language model verification, no production incremental suffix-array maintenance, no GPU serving latency, and only 180 sampled positions per corpus/context/min-match setting.

## Claim scope

On two small public prose corpora tokenized as bytes, suffix-array prompt+output-buffer lookup recovers exact prior-substring draft candidates with the same quality as exact n-gram lookup and lower rebuild cost than a naive all-length n-gram index, but exact accepted draft yield is sparse.

## Why it stopped

Proxy early evaluation did not support a paper-positive standalone claim; accepted draft yield was sparse and full speculative-decoding latency was not directly measured.

## Recommended next action

Stop this run as a proxy useful signal; the concrete next bounded test is an end-to-end BPE-token prompt-lookup decoder on a small local language model and high-repetition workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-token suffix-array prompt lookup in a real small-model speculative decoder
- Success threshold: At least 10% end-to-end tokens/sec improvement over no-draft and no worse than 5% behind hash prompt lookup on one high-repetition workload, without regression on ordinary prose beyond 5%.
- Stop condition: Stop if BPE-token accepted draft yield remains below 0.5 accepted tokens/position or end-to-end tokens/sec fails to beat no-draft by 5% on the high-repetition workload.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-from-prompt-output-buffer-9b0144c24cca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
