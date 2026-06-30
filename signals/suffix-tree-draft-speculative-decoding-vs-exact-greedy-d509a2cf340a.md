# Suffix-Tree Draft Speculative Decoding vs Exact Greedy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-speculative-decoding-vs-exact-greedy-d509a2cf340a`
Run ID: `suffix-tree-draft-speculative-decoding-vs-exact-greedy-d509a2cf340a-20260611T184921884320+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ec5fc68e5ade

## What looked useful

Exact verifier semantics worked in all runs. Static prompt-only suffix drafting gave 0 accepted tokens and 1.00x call speedup on tiny-gpt2, but 2.47x mean call speedup on distilgpt2. Dynamic prompt-plus-generated-history suffix drafting gave 5.82x mean call speedup on tiny-gpt2 and 3.86x on distilgpt2 while preserving exact greedy output.

## Boundaries and scale limits

Small hand-written prompt suite; tiny-gpt2 and distilgpt2 only; dynamic suffix table rebuilt in Python; no KV-cache-aware production verifier; no 1B-7B model, broad corpus, batching, or long-context validation.

## Claim scope

In a bounded exact-greedy harness on two GPT-2-class causal LMs and five hand-written prompts, suffix-context draft verification preserved exact greedy outputs. Static prompt-only suffix drafting was model/prompt dependent, while causal generated-history suffix drafting reduced target forward-pass counts on repetitive continuations.

## Why it stopped

No-paper useful signal: the local evidence supports a mechanism under repetitive contexts but is too small and model-dependent for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on a broader prompt corpus with a KV-cache-aware verifier and at least one modern larger causal LM before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix-context speculative greedy decoding on broader prompts
- Success threshold: Dynamic suffix drafting preserves exact greedy output and improves median wall-clock latency by at least 1.25x with median accepted draft length at least 1.0 on the broader prompt set.
- Stop condition: Stop as negative if exactness fails, median wall-clock speedup is below 1.10x, or accepted draft length is below 0.5 on the broader prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-speculative-decoding-vs-exact-greedy-d509a2cf340a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
