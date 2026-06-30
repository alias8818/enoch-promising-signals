# Suffix-Tree Prompt-Born Draft With Tree Verify On Base

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-prompt-born-draft-with-tree-verify-on-base-fa0c79bae1b7`
Run ID: `suffix-tree-prompt-born-draft-with-tree-verify-on-base-fa0c79bae1b7-20260614T013501970847+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/600cb3951efe

## What looked useful

Verification is not the bottleneck once a full candidate exists: median exact verify/build ratio was 0.0217 and all noisy drafts were detected. The prompt-born construction path remains unattractive in the tested representation because median edge-label payload was 64.55x input size, max 511.98x, and verify-plus-rebuild fallback cost was about rebuild cost with median fallback/build ratio 1.0284.

## Boundaries and scale limits

CPU-only proxy with deterministic exact/noisy drafts, naive compressed suffix-trie construction, no live LLM draft generator, no Ukkonen-style production baseline, and maximum input size 1024.

## Claim scope

On 64-1024 character synthetic strings, full suffix-set equality verification of an already-complete compressed suffix-tree draft is cheap and detects injected corruptions, but literal edge-label drafts are large and invalid-draft fallback does not beat rebuilding.

## Why it stopped

No-paper useful signal: proxy evidence supports cheap verification but not a viable literal prompt-born suffix-tree construction method.

## Recommended next action

Run a bounded follow-up using compact reference-encoded draft edges and compare verification plus local repair against a linear-time suffix-tree baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reference-Encoded Suffix-Tree Draft Verification
- Success threshold: Median serialized draft payload below 8x input size and median verify-plus-local-repair time at least 25% below rebuild time for corrupted drafts, with 100% detection of unrepaired invalid drafts.
- Stop condition: Stop if reference-encoded payload remains above 8x input size or local repair does not outperform rebuild on at least three of four text distributions.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-prompt-born-draft-with-tree-verify-on-base-fa0c79bae1b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
