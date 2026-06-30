# Adaptive N-Gram Speculative Cache from Verified Outputs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-n-gram-speculative-cache-from-verified-outputs-b9db1ebe9020`
Run ID: `adaptive-n-gram-speculative-cache-from-verified-outputs-b9db1ebe9020-20260526T042100915245+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8722ba9e610

## What looked useful

Adaptive verified-output cache updates consistently beat static, shuffled, and random controls in the simulator; gains were strongest for draft lengths 2 and 4 and weaker for draft length 8.

## Boundaries and scale limits

No live language model was served; target verifier cost was proxied by pass count, tokenization was regex word/punctuation tokenization, and the run covered two public text streams capped at 50,000 tokens rather than broad prompt/model workloads.

## Claim scope

In a bounded token-stream simulator over tiny_shakespeare and Alice in Wonderland text, an online n-gram cache populated only from previously verified tokens improved simulated target-pass reduction over a static prefix-only cache by 0.04245 absolute on average across draft lengths 2, 4, and 8.

## Why it stopped

Closed as no-paper useful signal because evidence is simulator/proxy evidence, not end-to-end live model decoding validation.

## Recommended next action

Run a bounded live small-LM follow-up using real tokenizer/model outputs and include cache lookup overhead before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-LM Verification of Adaptive Verified-Output N-Gram Speculative Cache
- Success threshold: Adaptive cache achieves at least 5% wall-clock decode throughput improvement over no-cache and at least 3% over static cache on the bounded prompt set, with exact output equivalence and cache overhead included.
- Stop condition: Stop if adaptive cache does not improve verifier-pass count by at least 3% over static cache or if lookup overhead eliminates wall-clock gains in the bounded live run.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-speculative-cache-from-verified-outputs-b9db1ebe9020`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
