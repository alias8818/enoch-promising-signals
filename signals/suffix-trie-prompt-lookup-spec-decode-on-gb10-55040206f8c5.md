# Suffix-Trie Prompt-Lookup Spec Decode on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-trie-prompt-lookup-spec-decode-on-gb10-55040206f8c5`
Run ID: `suffix-trie-prompt-lookup-spec-decode-on-gb10-55040206f8c5-20260630T141144639493+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98c91141a0ef

## What looked useful

Suffix-index prompt lookup is worth a bounded real-decoder follow-up for copy-heavy workloads because it preserved/slightly improved accepted tokens per step versus prompt scan while cutting proposal overhead from 1891.7 us/step to 2.83 us/step on the medium run; no-copy control showed 1.0x speedup, so overlap gating is required.

## Boundaries and scale limits

Synthetic/proxy only: verifier acceptance used known targets and CUDA matmul timing rather than real model logits, vLLM scheduling, batch serving, tokenization effects, or real code/document QA tasks. Medium run was 32 repeated-copy samples plus 16 no-copy controls on one GB10.

## Claim scope

On synthetic repeated-copy token workloads with 8k-token prompts and 1.5k-token targets on GB10, a suffix-index prompt lookup proposer reduces verifier steps about 4.48x versus vanilla and avoids the large CPU overhead of naive prompt scanning; no benefit appears on no-copy controls.

## Why it stopped

Synthetic verifier/proxy evidence supports the mechanism but is not direct serving-stack or real-model validation, so finalize_negative rather than paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the suffix-index proposer into a real vLLM or Transformers decoding loop and compare end-to-end latency/tokens-per-second on copy-heavy code-editing or document-QA prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder suffix-index prompt lookup on copy-heavy tasks
- Success threshold: At least 1.25x end-to-end speedup over vanilla and at least 1.10x over naive prompt lookup on a copy-heavy real-task set, with exact greedy output equality and proposal overhead under 5% of wall time.
- Stop condition: Stop as negative if real-decoder speedup is below 1.10x versus vanilla or proposal/scheduler overhead erases the verifier-step reduction on two copy-heavy task families.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-prompt-lookup-spec-decode-on-gb10-55040206f8c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
