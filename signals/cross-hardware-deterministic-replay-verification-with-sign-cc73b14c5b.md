# Cross-hardware deterministic replay verification with signed volunteer transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-hardware-deterministic-replay-verification-with-sign-cc73b14c5b`
Run ID: `cross-hardware-deterministic-replay-verification-with-sign-cc73b14c5b-20260610T000951547902+0000`

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

- Parent run decision: Deterministic Replay Verification of Volunteer Gradient Contributions: enoch://control-plane/projects/deterministic-replay-verification-of-volunteer-gradient-contributions-024cdf1189a7/runs/deterministic-replay-verification-of-volunteer-gradient-contributions-024cdf1189a7-20260609T183129739976+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d107f24872fd

## What looked useful

The transcript protocol and verifier are viable on a controlled small workload: 4 saved transcripts verified, fixed roots matched with sha256 3d0ec605205ae1e5131ed6571e19f1de4cd48bfd481d566182d2432e2f8274dc, floating controls diverged, and a tampered body was rejected.

## Boundaries and scale limits

No actual physical cross-hardware or cross-ISA run was completed because qemu-aarch64 and aarch64-linux-gnu-gcc were unavailable and apt installation was blocked by worker permissions. The result does not test remote volunteers, adversarial submissions, attestation, long traces, or real application replay.

## Claim scope

A local Tier 1 mechanism test showed that signed volunteer transcript bodies can be generated, Ed25519-verified, tamper-rejected, and compared by workload root; the fixed-point replay root matched across two independently compiled native x86_64 targets while a floating-point control diverged.

## Why it stopped

No-paper useful-signal closure: the signed transcript verification mechanism passed a controlled local Tier 1 test, but the title claim still lacks actual cross-hardware evidence.

## Recommended next action

Run the same harness on two real hardware/ISA targets, such as x86_64 and ARM64, and require matching fixed-point roots, valid signatures, tamper rejection, and a divergent floating-point control before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-ISA signed replay transcript validation
- Success threshold: At least two real hardware/ISA targets produce the same fixed-point workload root with all signatures verified and tamper rejection passing; the divergence control must produce non-matching roots that the verifier flags.
- Stop condition: Stop as negative if fixed-point roots differ after confirming identical source, build flags, inputs, and transcript canonicalization, or if signatures/tamper checks fail on any target.

## Evidence references

- Artifact root: `<local-path>/projects/cross-hardware-deterministic-replay-verification-with-sign-cc73b14c5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
